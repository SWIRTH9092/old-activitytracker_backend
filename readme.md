### Project4 Python backend for activity tacker

##### Links
- GitHub: https://github.com/SWIRTH9092/activitytracker_backend
- Render: 

##### Dependencies
- Django
    - dj-database-url 
    - psycopg2-binary 
- Postgres

##### Activity Tracker Tables
-   Postgres database name:  
    - projects
-   table names:
    - activity 
    - activity tracker
- Features:
    -  referential integrity between the tables
        - activity.act_id = activity.tracker.act_main_id
    -  cascading deletes if activity row is deleted (data is also deleted from the activitytracker table as well)

<img src="https://i.imgur.com/7jVQkmQ.png" alt="sql database drawing" title="SQL database drawing" width="90%"/> 

#### Routes 

| Table |Routes | Method | EndPoints | Expected Result |
|------|-------|--------|-----------|-----------------|
| activity | Index | GET | /activity | Gets all entries |
| activity | Create | POST | /activity | Creates a new entry |
| activity | Show | GET | /activity:id | Gets 1 entry
| activity | Update | PUT | /activity:id | Updates Existing Entry |
| activity | Delete | DELETE | /activity:id | Removes entry from database
| activitytracker| Index | GET | /activitytracker | Gets all entries |
| activitytracker| Create | POST | /activitytracker | Creates a new entry |
| activitytracker| Show | GET | /activitytracker:id | Shows all entries for an activity
| activitytracker| Update | PUT | /activitytracker:id | Updates Existing Entry |
| activitytracker| Delete | DELETE | /activitytracker:id | Removes entry from database
