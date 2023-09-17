const { contextBridge, ipcRenderer } = require('electron')

console.log("exposing scan start")
contextBridge.exposeInMainWorld('scan', {
  start: (dir) => ipcRenderer.send('scan:start', dir)
})
