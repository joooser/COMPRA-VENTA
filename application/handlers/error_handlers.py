@app.errorhandler(404)
def not_found_error(error):
    log_error(error) 
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    log_error(error)
    db.session.rollback()
    return render_template('500.html'), 500

def log_error(error):
    # Log error to central logging system
    pass