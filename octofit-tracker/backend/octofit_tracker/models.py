from djongo import models


class UserProfile(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"


class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    league = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return f"{self.name} ({self.league})"


class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'activities'

    def __str__(self):
        return f"{self.activity_type} by {self.user_email}"


class LeaderboardEntry(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    rank = models.PositiveIntegerField()
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    score = models.PositiveIntegerField()

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        return f"#{self.rank} {self.user_email} ({self.team})"


class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
    duration_minutes = models.PositiveIntegerField()
    muscle_groups = models.JSONField(default=list, blank=True)

    class Meta:
        db_table = 'workouts'

    def __str__(self):
        return self.name
