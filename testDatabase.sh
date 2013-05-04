#!/bin/bash
set -e
sudo -u postgres dropdb pmstest
sudo -u postgres createdb pmstest "Test Environment Database for Project Manager System"
sudo -u postgres psql -d pmstest -f pms.database.sql
