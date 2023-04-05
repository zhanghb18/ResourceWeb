module.exports = {
    lintOnSave: false,
    publicPath: process.env.NODE_ENV === 'production' ? '../static/' : '/',
    outputDir: 'static',
    indexPath: 'index.html',
    filenameHashing: true,
    devServer: process.env.NODE_ENV === 'production' ? {} : {
        host: "0.0.0.0",
        port: 8024, // 端口号
        https: false, // https:{type:Boolean}
        open: false, //配置自动启动浏览器  http://172.11.11.22:8888/rest/XX/
        proxy: {
            '/api': {
                target: 'http://123.56.45.70:8012/',
                ws: true,
                changeOrigin: true,
                pathRewrite: {
                    "^/api": ""
                }
            }
        }
    }
}