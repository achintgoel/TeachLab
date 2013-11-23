/*global frontend, $*/


window.frontend = {
  Models: {},
  Collections: {},
  Views: {},
  Routers: {},
  init: function () {
    'use strict';
    console.log('Hello from Backbone!');
    var appModel = new this.Models.AppModel();
    var appView = new this.Views.AppView({
      model: appModel,
      el: $('.teachlab-main')
    });
    appView.render();

    var appRouter = new this.Routers.AppRouter();

    Backbone.history.start({
      pushState: false,
      root: '/',
      silent: true
    });
  }
};

$(document).ready(function () {
  frontend.init();
});
