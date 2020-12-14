// const path = require('path')

module.exports = {
  "assetsDir": "../static/todos",
  "indexPath": "../templates/todos/index.html",
  "filenameHashing": false,
  "transpileDependencies": [
    "vuetify"
  ],
  'configureWebpack':{
    'performance': {
      'hints': false
    },
    'optimization': {
      'splitChunks': {
        'minSize': 10000,
        'maxSize': 250000,
      }
    }
  }
}