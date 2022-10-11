# OLA-bikes-demand-forecast
Ola Bikes are suffering losses and losing out from their competition due to their
inability to fulfill the ride requests of many users. To tackle this problem you we
predict demand for rides in a certain region and a given future time window.
This would help them allocate drivers more intelligently to meet the ride requests
from users.
Ola Management knows the task is not easy and very important for their business to
grow.
Hence, their business team has provided you some guidelines to follow.
1. Count only 1 ride request by a user, if there are multiple bookings from the
same latitude and longitude within 1hour of the last booking time.
2. If there are ride requests within 8mins of the last booking time consider only 1
ride
request from a user (latitude and longitude may or may not be the same).
3. If the geodesic distance from pickup and drop point is less than 50meters
consider that ride request as a fraud ride request.
4. Consider all ride requests where pick up or drop location is outside India as
system error.
5. Karnataka is our prime city where we have a lot of drivers and ride requests to
fulfill. We would not love to serve rides that are outside Karnataka and have
pickup and drop geodesic distance > 500kms.
