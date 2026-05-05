from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from pymongo import MongoClient

from octofit_tracker.models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Starting database population for octofit_db...')

        # Delete existing data
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        UserProfile.objects.all().delete()

        # Create teams
        teams = [
            {
                'name': 'Marvel',
                'league': 'Marvel',
                'description': 'Team Marvel features the earth\'s greatest super heroes.',
            },
            {
                'name': 'DC',
                'league': 'DC',
                'description': 'Team DC features iconic heroes and warriors from the DC Universe.',
            },
        ]

        for item in teams:
            Team.objects.create(**item)

        # Create users
        users = [
            {
                'first_name': 'Tony',
                'last_name': 'Stark',
                'email': 'tony.stark@marvel.com',
                'team': 'Marvel',
                'role': 'Tech Leader',
            },
            {
                'first_name': 'Peter',
                'last_name': 'Parker',
                'email': 'peter.parker@marvel.com',
                'team': 'Marvel',
                'role': 'Rookie',
            },
            {
                'first_name': 'Bruce',
                'last_name': 'Wayne',
                'email': 'bruce.wayne@dc.com',
                'team': 'DC',
                'role': 'Strategist',
            },
            {
                'first_name': 'Clark',
                'last_name': 'Kent',
                'email': 'clark.kent@dc.com',
                'team': 'DC',
                'role': 'Field Captain',
            },
        ]

        for item in users:
            UserProfile.objects.create(**item)

        now = timezone.now()
        activities = [
            {
                'user_email': 'tony.stark@marvel.com',
                'team': 'Marvel',
                'activity_type': 'Flight Training',
                'duration_minutes': 45,
                'calories_burned': 380,
                'timestamp': now - timedelta(hours=5),
            },
            {
                'user_email': 'peter.parker@marvel.com',
                'team': 'Marvel',
                'activity_type': 'Wall Climbing',
                'duration_minutes': 30,
                'calories_burned': 240,
                'timestamp': now - timedelta(hours=3, minutes=20),
            },
            {
                'user_email': 'bruce.wayne@dc.com',
                'team': 'DC',
                'activity_type': 'Combat Practice',
                'duration_minutes': 55,
                'calories_burned': 420,
                'timestamp': now - timedelta(hours=4, minutes=10),
            },
            {
                'user_email': 'clark.kent@dc.com',
                'team': 'DC',
                'activity_type': 'Speed Run',
                'duration_minutes': 20,
                'calories_burned': 310,
                'timestamp': now - timedelta(hours=2, minutes=15),
            },
        ]

        for item in activities:
            Activity.objects.create(**item)

        workouts = [
            {
                'name': 'Power Armor Circuit',
                'description': 'Strength and endurance training designed for armored heroes.',
                'difficulty': 'Medium',
                'duration_minutes': 40,
                'muscle_groups': ['full body', 'arms', 'core'],
            },
            {
                'name': 'Web-Swing Conditioning',
                'description': 'Agility and stamina workout for quick recovery and mobility.',
                'difficulty': 'Easy',
                'duration_minutes': 30,
                'muscle_groups': ['legs', 'core'],
            },
            {
                'name': 'Batsuit Bootcamp',
                'description': 'High-intensity circuit training with strength and stealth drills.',
                'difficulty': 'Hard',
                'duration_minutes': 50,
                'muscle_groups': ['chest', 'back', 'legs'],
            },
            {
                'name': 'Super-Speed Sprints',
                'description': 'Cardio-heavy workout targeting speed and recovery agility.',
                'difficulty': 'Medium',
                'duration_minutes': 35,
                'muscle_groups': ['legs', 'core'],
            },
        ]

        for item in workouts:
            Workout.objects.create(**item)

        leaderboard_entries = [
            {
                'rank': 1,
                'user_email': 'clark.kent@dc.com',
                'team': 'DC',
                'score': 980,
            },
            {
                'rank': 2,
                'user_email': 'tony.stark@marvel.com',
                'team': 'Marvel',
                'score': 950,
            },
            {
                'rank': 3,
                'user_email': 'bruce.wayne@dc.com',
                'team': 'DC',
                'score': 920,
            },
            {
                'rank': 4,
                'user_email': 'peter.parker@marvel.com',
                'team': 'Marvel',
                'score': 890,
            },
        ]

        for item in leaderboard_entries:
            LeaderboardEntry.objects.create(**item)

        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db has been populated with sample test data.'))
