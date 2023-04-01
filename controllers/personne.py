import os

def liste_personnes():
        #db().select(db.films.ALL)
    requete = db.personne.id > 0
    rows = db(requete).select()
    #rows = db().select(db.films.ALL);
    return response.render('personne/liste.html', dict(personne=rows))


# CREATE  personne
def create_personne():
    
    form = SQLFORM(db.personne)
    if form.process().accepted:
        session.flash = 'Personnes créée'
        redirect(URL('personne', 'liste_personnes'))
    return dict(form=form)


# UPDATE


def edit_personne():
    personne = db.personne(request.args(0)) or redirect(URL('liste_personnes'))
    form = SQLFORM(db.personne, personne)
    if form.process().accepted:
        redirect(URL('liste_personnes'))
    return dict(form=form)


def delete_personne():
    personne_id = request.vars.id
    personne = db.personne(personne_id)
    if not personne:
        raise HTTP(404, "L'personne n'existe pas")
    db(db.personne.id == personne_id).delete()
    session.flash = 'Personnes supprimée'
    redirect(URL('personne', 'liste_personnes'))