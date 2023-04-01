import os

def liste_projets():
        #db().select(db.films.ALL)
    requete = db.projet.id > 0
    rows = db(requete).select()
    #rows = db().select(db.films.ALL);
    return response.render('projet/liste.html', dict(projet=rows))


# CREATE  projet
def create_projet():
    
    form = SQLFORM(db.projet)
    if form.process().accepted:
        session.flash = 'Projets créée'
        redirect(URL('projet', 'liste_projets'))
    return dict(form=form)


# UPDATE


def edit_projet():
    projet = db.projet(request.args(0)) or redirect(URL('liste_projets'))
    form = SQLFORM(db.projet, projet)
    if form.process().accepted:
        redirect(URL('liste_projets'))
    return dict(form=form)


def delete_projet():
    projet_id = request.vars.id
    projet = db.projet(projet_id)
    if not projet:
        raise HTTP(404, "L'projet n'existe pas")
    db(db.projet.id == projet_id).delete()
    session.flash = 'Projets supprimée'
    redirect(URL('projet', 'liste_projets'))