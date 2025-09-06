#!/usr/bin/env python3
"""
Demo script for Google OAuth Dashboard
This script helps you test the application functionality
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'google.settings')
django.setup()

from django.contrib.auth.models import User
from google_login.models import Event
from datetime import datetime, timedelta

def create_demo_data():
    """Create demo data for testing"""
    print("🚀 Creating demo data...")
    
    # Create a demo user if it doesn't exist
    user, created = User.objects.get_or_create(
        username='demo_user',
        defaults={
            'email': 'demo@example.com',
            'first_name': 'Demo',
            'last_name': 'User',
            'is_staff': False,
            'is_superuser': False
        }
    )
    
    if created:
        user.set_password('demo123')
        user.save()
        print("✅ Demo user created: demo_user / demo123")
    else:
        print("ℹ️  Demo user already exists")
    
    # Create demo events
    events_data = [
        {
            'summary': 'Team Meeting',
            'start_time': datetime.now() + timedelta(hours=1),
            'end_time': datetime.now() + timedelta(hours=2)
        },
        {
            'summary': 'Project Review',
            'start_time': datetime.now() + timedelta(days=1, hours=10),
            'end_time': datetime.now() + timedelta(days=1, hours=11)
        },
        {
            'summary': 'Client Call',
            'start_time': datetime.now() + timedelta(days=2, hours=14),
            'end_time': datetime.now() + timedelta(days=2, hours=15)
        }
    ]
    
    for event_data in events_data:
        event, created = Event.objects.get_or_create(
            summary=event_data['summary'],
            defaults=event_data
        )
        if created:
            print(f"✅ Event created: {event.summary}")
        else:
            print(f"ℹ️  Event already exists: {event.summary}")
    
    print("\n🎉 Demo data setup complete!")
    print("\n📋 Next steps:")
    print("1. Run the server: python manage.py runserver")
    print("2. Visit: http://127.0.0.1:8000/")
    print("3. Login with Google OAuth")
    print("4. Explore the dashboard, profile, and settings pages")

def check_dependencies():
    """Check if all required packages are installed"""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        'django',
        'django-allauth',
        'django-oauth-toolkit',
        'google-auth',
        'google-auth-oauthlib',
        'google-auth-httplib2',
        'google-api-python-client'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install -r requirements.txt")
        return False
    
    print("\n✅ All dependencies are installed!")
    return True

def check_database():
    """Check database connection and migrations"""
    print("🗄️  Checking database...")
    
    try:
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        print("✅ Database connection successful")
        
        # Check if migrations are applied
        from django.core.management import call_command
        call_command('showmigrations', verbosity=0)
        print("✅ Database migrations are up to date")
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        print("Run migrations with: python manage.py migrate")
        return False
    
    return True

def main():
    """Main demo function"""
    print("🎯 Google OAuth Dashboard Demo")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Check database
    if not check_database():
        return
    
    # Create demo data
    create_demo_data()
    
    print("\n🎊 Demo setup complete!")
    print("\n💡 Tips:")
    print("- Make sure you have configured Google OAuth credentials")
    print("- Update settings.py with your Google OAuth details")
    print("- The demo user can be used for testing without OAuth")

if __name__ == '__main__':
    main()
