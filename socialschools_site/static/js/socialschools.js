$(function() {
  $('#videos a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
  });
  $('#support a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
  });
  $('#about a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
  });
  $('#team a').click(function (e) {
    e.preventDefault();
    $(this).tab('show');
  });  
  $('.form-price > div > form > p > input[type="submit"]').addClass('btn');
  $('.demo-form > div > form > p > input[type="submit"]').addClass('btn');
  $('.demo-form > div > form > ul').addClass('list-unstyled');
  $('.question-container > div > form > p > input[type="submit"]').addClass('btn'); 
});

