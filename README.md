# Smart Band Edge Service (smart_band_edge_service)

## Overview

Smart Band Edge Service is a python-based application for processing and analyzing data from smart wearable devices at the edge

## Dependencies

- Python 3.13 or higher
- Flask (web framework)
- Peewee (ORM for database interactions)
- SQLite (database)
- pyhton-dateutil (date and time utiities)

## Domain-Driven Design (DDD) Structure

The Project follows a Domain-Driven Design (DDD) approach, organizing the code unto distinct bounded context:
- **Health Monitoring**: Manages health-related data from smart bands, including heart rate
- **Identity and Access Management**: Handles device authentication and autorization

## User Stories
The user stories for the Smart Band Edge Service can be found in the [docs/user-stories.md](docs/user-stories.md) file.

## Class Diagram
The class diagram for the Smart Band Edge Service is available in [docs/class-diagram.md](docs/class-diagram.md) file.