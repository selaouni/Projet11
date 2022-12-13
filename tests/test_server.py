import os
import tempfile
from server import loadClubs
from server import loadCompetitions

def test_loadClubs():
    club = [{'name': 'Simply Lift', 'email': 'john@simplylift.co', 'points': '13'},
           {'name': 'Iron Temple', 'email': 'admin@irontemple.com', 'points': '4'},
           {'name': 'She Lifts', 'email': 'kate@shelifts.co.uk', 'points': '12'}]
    assert loadClubs() == club


def test_loadCompetitions():
    competition = [{'name': 'Spring Festival', 'date': '2022-12-27 10:00:00', 'numberOfPlaces': '25'},
                   {'name': 'Fall Classic', 'date': '2020-10-22 13:30:00', 'numberOfPlaces': '13'}]
    assert loadCompetitions() == competition


def test_login_user(client, email):
    rv = client.post(
        "/", data=dict(email=email), follow_redirects=True
    )
    assert rv.status_code == 200
def test_logout_user(client):
    rv = client.get("/logout", follow_redirects=True)
    assert rv.status_code == 200

def test_should_status_code_ok(client):
    response1 = client.get('/')
    assert response1.status_code == 200



def test_home_without_email(client):
    rv = client.get("/", follow_redirects=True)
    data = rv.data.decode()
    assert data.find("email") != -1


def test_book_places_page(client, competition, club):
    response = client.get('/book/<competition>/<club>',
                          data=dict(competition=competition, club=club),
                          follow_redirects=True)

    assert response.status_code == 200
    data = response.data.decode
    assert data.find('Book Places') == -1


def test_purchase_places(client, competition, club):
    response = client.get('/purchasePlaces',
                           data=dict(competition=competition, club=club),
                           follow_redirects=True)

     assert response.status_code == 200
     data = response.data.decode
     assert data.find('Book Places') == -1


def test_points_display(client, competition, club):
    response = client.get('/points_dashboard',
                            data=dict(competition=competition, club=club),
                            follow_redirects=True)

    assert response.status_code == 200


def test_show_summary(client, competition, club):
    response = client.get('/showSummary',
                          data=dict(competition=competition, club=club),
                          follow_redirects=True)

    assert response.status_code == 200












































#     # assert response2.status_code == 200
#     # assert response3.status_code == 200
#     # assert response4.status_code == 200
#     # assert response5.status_code == 200
# response2 = client.get('/showSummary')
#     # response3 = client.get('/book/<competition>/<club>')
#     # response4 = client.get('/purchasePlaces')
#     # response5 = client.get('/logout')