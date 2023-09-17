const {ipcMain} = require('electron');
const {spawn} = require('child_process');
const fs = require("fs");

function scanFiles(dir = "/") {
  python_path = process.env.PYTHON_PATH || "python3";
  return spawn(python_path, ["../crawler/filecrawler.py", "--index-name", "one_go", "--path", dir, "-T", "2", "-v", "--local"]);
}

ipcMain.on("scan:start", (event, dir) => {
  if (dir == null) {
    dir = __dirname;
  }
  const scan = scanFiles(dir);
  scan.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
    event.reply("scan:stdout", data);
  });

  scan.stderr.on('data', (data) => {
    return data;
  });

  scan.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    event.reply("scan:close", code);
  });
});

const DATABASE = "cron.json";
let CACHE = [];

function restoreCronJobs() {
  const fs = require('fs');
  const CronJob = require('cron').CronJob;

  if (fs.existsSync(DATABASE) === false) {
    fs.writeFileSync(DATABASE, JSON.stringify([]));
    return;
  }

  fs.readFile(DATABASE, (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    CACHE = JSON.parse(data);

    for (const job of CACHE) {
      const {_, cron} = job;
      new CronJob(cron, scanFiles, null, true);
    }
    console.log("restored cron jobs");
  });
}

ipcMain.handle("jobs:get", (event) => {
  if (CACHE.length === 0) {
    const fs = require('fs');
    try {
      let content = fs.readFileSync(DATABASE);
      CACHE = JSON.parse(content);
    } catch (e) {
    }
  }
  return CACHE;
});

ipcMain.handle("jobs:delete", (event, index) => {
  if (index < CACHE.length) {
    CACHE.splice(index, 1);
    const fs = require('fs');
    try {
      fs.writeFileSync(DATABASE, JSON.stringify(CACHE));
    } catch (e) {
    }
    return CACHE;
  }
})

ipcMain.handle("jobs:create", async (event, data) => {
  const {name, cron} = data;
  CACHE.push({name, cron});
  const fs = require('fs');
  try {
    fs.writeFileSync(DATABASE, JSON.stringify(CACHE));
  } catch (e) {
  }
  return CACHE;
})

ipcMain.handle("jobs:validateCron", async (event, cron) => {
  const CronJob = require('cron').CronJob;
  try {
    new CronJob(cron, () => {
    }, null, false);
    return true;
  } catch (e) {
    return false;
  }
})

module.exports = {
  restoreCronJobs
}