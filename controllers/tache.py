import os

def liste_taches():
        #db().select(db.films.ALL)
    requete = db.tache.id > 0
    rows = db(requete).select()
    #rows = db().select(db.films.ALL);
    return response.render('tache/liste.html', dict(tache=rows))


# CREATE  tache
def create_tache():
    
    form = SQLFORM(db.tache)
    if form.process().accepted:
        session.flash = 'Taches créée'
        redirect(URL('tache', 'liste_taches'))
    return dict(form=form)


# UPDATE


def edit_tache():
    tache = db.tache(request.args(0)) or redirect(URL('liste_taches'))
    form = SQLFORM(db.tache, tache)
    if form.process().accepted:
        redirect(URL('liste_taches'))
    return dict(form=form)


def delete_tache():
    tache_id = request.vars.id
    tache = db.tache(tache_id)
    if not tache:
        raise HTTP(404, "L'tache n'existe pas")
    db(db.tache.id == tache_id).delete()
    session.flash = 'Taches supprimée'
    redirect(URL('tache', 'liste_taches'))