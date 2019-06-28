var gulp = require('gulp');
var shell = require('gulp-shell')


gulp.task('run-tests', shell.task([
   'python run-tests.py']))

gulp.task('watch', function(){
   gulp.watch(['./*.py'], gulp.series('run-tests'));
});
