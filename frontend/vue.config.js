module.exports = {
    devServer: {
      proxy: {
        '/api': {
          target: 'http://localhost:8000',  // URL backend FastAPI
          changeOrigin: true,
          secure: false,
        },
      },
    },
  };
  