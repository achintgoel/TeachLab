/*global frontend, Backbone*/

frontend.Routers = frontend.Routers || {};

(function () {
  frontend.Routers.AppRouter = Backbone.Router.extend({
    routes: {
      '': 'home'
    },

    home: function(){
      console.log('home');
    }
  });

})();
