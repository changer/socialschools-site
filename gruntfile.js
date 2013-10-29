module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    concat: {
      dist: {
        src: ['socialschools_site/static/js/jquery.min.js','socialschools_site/static/bootstrap/js/tab.js', 'socialschools_site/static/js/socialschools.js'],
        dest: 'socialschools_site/static/js/<%= pkg.name %>.add.js'
      }
    },
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
      },
      dist: {
        files: {
          'socialschools_site/static/js/<%= pkg.name %>.min.js': ['<%= concat.dist.dest %>']
        }
      }
    },
    jshint: {
      files: ['gruntfile.js', 'src/**/*.js', 'test/**/*.js'],
      options: {
        // options here to override JSHint defaults
        globals: {
          jQuery: true,
          console: true,
          module: true,
          document: true
        }
      }
    },
    less: {
      debug: {
        src: 'socialschools_site/static/css/styles.less',
        dest: 'socialschools_site/static/css/styles.css'
      }
    },
    cssmin: {
      'socialschools_site/css/styles.css': [
        'socialschools_site/static/css/styles.css'
      ]
    },
    watch: {
      files: ['<%= jshint.files %>'],
      tasks: ['jshint']
    }
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-requirejs');

  grunt.registerTask('test', ['jshint']);
  grunt.registerTask('js', ['concat','uglify']);
  //default tasks for js files
  grunt.registerTask('default', ['jshint', 'concat', 'uglify']);
  //css compilation from less and minification
  grunt.registerTask('css', ['less', 'cssmin']);

};
