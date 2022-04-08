const path = require('path');

const PATHS = {
source: path.join(__dirname, 'src'),
build: path.join(__dirname, 'build')
};

module.exports = {
mode: 'production',
entry: PATHS.source + '/index.js',
devtool: 'inline-source-map',
output: {
path: PATHS.build,
filename: '[name].js'
},
devServer: {
static: {
directory: PATHS.source,
},
port: 8000,
hot: false
}
};