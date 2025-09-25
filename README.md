# Smart Band Edge Service (smart_band_edge_service)

## Overview

Smart Band Edge Service is a Pyhton-based application for procesing and analyzing data from samrt wearable devices at the edge.

## Depedencies 
- Python 3.13 or higher.
- Flask (Web Framework)
- Peewee (ORM for database interactions)
- SQLite (Database)
- python-dateutil (date and tiem itilities)

## Domain-Driven Design (DDD) Structure
The project folloes a Domain Driven Design (DDD) approach, organizing the code into distinct bounded context:

- **Health Monitoring**: Manages health-related data from smart bands, includig heart rate.
- **Identity and Access Management**: Handles device auhtentication and authorization.

## User Stories 
The user storues for the Smart and Edge Service can be found in the 