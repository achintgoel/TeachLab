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
  }
};

$(document).ready(function () {
  frontend.init();
});
