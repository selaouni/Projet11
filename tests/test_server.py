import pytest
from ..server import create_app
from ..server import loadClubs
from ..server import loadCompetitions

@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_loadClubs():
    club = [{'name': 'Simply Lift', 'email': 'john@simplylift.co', 'points': '13'},
           {'name': 'Iron Temple', 'email': 'admin@irontemple.com', 'points': '4'},
           {'name': 'She Lifts', 'email': 'kate@shelifts.co.uk', 'points': '12'}]
    assert loadClubs() == club


def test_loadCompetitions():
    competition = [{'name': 'Spring Festival', 'date': '2022-12-27 10:00:00', 'numberOfPlaces': '25'},
                   {'name': 'Fall Classic', 'date': '2020-10-22 13:30:00', 'numberOfPlaces': '13'}]
    assert loadCompetitions() == competition

def _login_user(client, email):
    response = client.post(
        "/showSummary", data=dict(email=email), follow_redirects=True
    )
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("email") == -1

def _logout_user(client):
    rv = client.get("/logout", follow_redirects=True)
    assert rv.status_code == 200
def test_login_user(client):
    _login_user(client, 'admin@irontemple.com')

# def test_login_user(client):
#     email = "admin@irontemple.com"
#     response = client.post(
#         '/showSummary', data=dict(email=email), follow_redirects=True
#     )
#     data = response.data.decode()
#     assert response.status_code == 200
#     assert "Welcome" in data

# def test_logout_user(client):
#     rv = client.get("/logout", follow_redirects=True)
#     assert rv.status_code == 200
#

# def test_login_email_unknown(client):
#     unknown_email = 'sabah.elaouni@test.com'
#     response = client.post('/showSummary',
#                            data=dict(email=unknown_email),
#                            follow_redirects=True
#                            )
#     data = response.data.decode()
#     assert response.status_code == 200
#     assert "Sorry, that email wasn't found." in data

# def test_should_status_code_ok(client):
#     response1 = client.get('/')
#     assert response1.status_code == 200
#
#
#
# def test_home_without_email(client):
#     rv = client.get("/", follow_redirects=True)
#     data = rv.data.decode()
#     assert data.find("email") != -1
#
#
# def test_book_places_page(client, competition, club):
#     response = client.get('/book/<competition>/<club>',
#                           data=dict(competition=competition, club=club),
#                           follow_redirects=True)
#
#     assert response.status_code == 200
#     data = response.data.decode
#     assert data.find('Book Places') == -1
#
#
# def test_purchase_places(client, competition, club):
#     response = client.get('/purchasePlaces',
#                            data=dict(competition=competition, club=club),
#                            follow_redirects=True)
#
#     assert response.status_code == 200
#     data = response.data.decode
#     assert data.find('Book Places') == -1
#
#
# def test_points_display(client, competition, club):
#     response = client.get('/points_dashboard',
#                             data=dict(competition=competition, club=club),
#                             follow_redirects=True)
#
#     assert response.status_code == 200
#
#
# def test_show_summary(client, competition, club):
#     response = client.get('/showSummary',
#                           data=dict(competition=competition, club=club),
#                           follow_redirects=True)
#
#     assert response.status_code == 200
#
# class TestLoginEmail:
#
#     def setup(self):
#         self.listOfClubs = [{'name': 'club_1', 'email': 'email_club_1', 'points': "30"},
#                     {'name': 'club_2', 'email': 'email_club_2', 'points': "5"}]
#         self.listOfCompetitions = [{"name": "competition_1","date": "2020-03-27 10:00:00","numberOfPlaces": "25"},
#                             {"name": "competition_2","date": "2020-10-22 13:30:00","numberOfPlaces": "13"}]
#         self.login_email = "email_club_1"
#         self.unknown_email = "email_club_3"
#
#     def test_login_mail_exist(self, client, mocker):
#         mocker.patch.object(server, 'clubs', self.listOfClubs)
#
#         response = client.post('/showSummary',
#                               data=dict(email=self.login_email),
#                               follow_redirects=True
#                               )
#         data = response.data.decode()
#         assert response.status_code == 200
#         assert "Welcome" in data
#
#     def test_login_email_unknown(self, client, mocker):
#         mocker.patch.object(server, 'clubs', self.listOfClubs)
#         response = client.post('/showSummary',
#                               data=dict(email=self.unknown_email),
#                               follow_redirects=True
#                               )
#         data = response.data.decode()
#         assert response.status_code == 200
#         assert "Unknown email" in data
#
#
#
#
#     assert response.status_code == 200
#     expected_error_message = "You do not have permission to book more than 12 places"
#     assert expected_error_message not in data
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



#     # assert response2.status_code == 200
#     # assert response3.status_code == 200
#     # assert response4.status_code == 200
#     # assert response5.status_code == 200
# response2 = client.get('/showSummary')
#     # response3 = client.get('/book/<competition>/<club>')
#     # response4 = client.get('/purchasePlaces')
#     # response5 = client.get('/logout')