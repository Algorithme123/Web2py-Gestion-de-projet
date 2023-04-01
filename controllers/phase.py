import os

def liste_phases():
        #db().select(db.films.ALL)
    requete = db.phase.id > 0
    rows = db(requete).select()
    #rows = db().select(db.films.ALL);
    return response.render('phase/liste.html', dict(phase=rows))


# CREATE  phase
def create_phase():
    
    form = SQLFORM(db.phase)
    if form.process().accepted:
        session.flash = 'Phases créée'
        redirect(URL('phase', 'liste_phases'))
    return dict(form=form)


# UPDATE


def edit_phase():
    phase = db.phase(request.args(0)) or redirect(URL('liste_phases'))
    form = SQLFORM(db.phase, phase)
    if form.process().accepted:
        redirect(URL('liste_phases'))
    return dict(form=form)


def delete_phase():
    phase_id = request.vars.id
    phase = db.phase(phase_id)
    if not phase:
        raise HTTP(404, "L'phase n'existe pas")
    db(db.phase.id == phase_id).delete()
    session.flash = 'Phases supprimée'
    redirect(URL('phase', 'liste_phases'))