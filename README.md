# unmix-board
Web application to generate comparable overviews of training runs with the unmix-net.

## api
The serving web api runs on Python 3.7 with [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/).

### Requirements
Install all dependencies by using `pip install -r requirements.txt`.

### Configuration
The following environment variables have to be added:
- `UNMIX_BOARD_API_PORT`: Port to run the web server on
- `UNMIX_BOARD_API_PATHS`: List of paths to crawl for run folders created by [unmix-net](https://github.com/unmix-io/unmix-net) training runs

## web
The frontend application runs on [Vue.js](https://vuejs.org/).

### Project setup
```
yarn install
```

#### Compiles and hot-reloads for development
```
yarn run serve
```

#### Compiles and minifies for production
```
yarn run build
```

#### Run your tests
```
yarn run test
```

#### Lints and fixes files
```
yarn run lint
```

#### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
