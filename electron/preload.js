const {contextBridge, ipcRenderer} = require('electron')

console.log("exposing scan start")
contextBridge.exposeInMainWorld('scan', {
  start: (dir) => ipcRenderer.send('scan:start', dir)
});
contextBridge.exposeInMainWorld('jobs', {
  get: () => ipcRenderer.invoke('jobs:get'),
  delete: (index) => ipcRenderer.invoke('jobs:delete', index),
  create: (data) => ipcRenderer.invoke('jobs:create', data),
  validateCron: (cron) => ipcRenderer.invoke('jobs:validateCron', cron),
})
