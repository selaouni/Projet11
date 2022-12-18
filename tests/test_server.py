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


def test_should_status_code_ok(client):
    response1 = client.get('/')
    assert response1.status_code == 200


def test_book_places_page(client):
    response = client.get('book/Spring%20Festival/Iron%20Temple')
    assert response.status_code == 200


def _login_user(client, email):
    response = client.post(
        "/showSummary", data=dict(email=email), follow_redirects=True
    )
    assert response.status_code == 200
    data = response.data.decode()
    assert data.find("email") == -1


def _logout_user(client):
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200


def test_login_user(client):
    _login_user(client, 'admin@irontemple.com')


def test_logout_user(client):
    _logout_user(client)


def test_login_email_unknown(client):
    unknown_email = 'sabah.elaouni@test.com'
    response = client.get('/',
                           data=dict(email=unknown_email),
                           follow_redirects=True
                           )
    data = response.data.decode()
    assert response.status_code == 200
    assert "Sorry, that email wasn't found." not in data


def test_no_more_than_12_places(client):
    response = client.get("/logout", follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    expected_error_message = "You do not have permission to book more than 12 places"
    assert expected_error_message not in data


def test_purchase_past_competitions(client):
    response = client.get("book/Spring%20Festival/Iron%20Temple", follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    expected_error_message = "<p>You cannot book places in a past competition<p>"
    assert expected_error_message not in data


def test_points_display(client):
    club = [{'name': 'club_1', 'email': 'email_club_1', 'points': "30"},
            {'name': 'club_2', 'email': 'email_club_2', 'points': "5"}]
    competition = [{"name": "competition_1", "date": "2020-03-27 10:00:00", "numberOfPlaces": "25"},
                   {"name": "competition_2", "date": "2020-10-22 13:30:00", "numberOfPlaces": "13"}]
    response = client.get('/points_dashboard',
                            data=dict(competition=competition, club=club),
                            follow_redirects=True)
    assert response.status_code == 200
