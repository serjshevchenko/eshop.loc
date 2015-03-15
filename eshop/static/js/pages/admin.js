define(['jqueryTE'], function() {
    $('.textarea-jqte').jqte();
    return {};
}, function(err){console.log('err:'+err);});
if (requirejs) requirejs.onerror = function(){};
