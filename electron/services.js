const {ipcMain} = require('electron');
ipcMain.on("scan:start", (event, dir)=>{
  console.log("test " + dir);
});
