from datetime import datetime
from django.db import connection
from django.http import JsonResponse, HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

def create_table_view(request, c, s, d):
    # Ensure the date format is correct (e.g., '2024-02-02' instead of '2024_02_02')
    try:
        # Replace hyphens with underscores for SQLite compatibility
        formatted_date = d.replace('_', '-')  # Replace underscores with hyphens for the date
        formatted_date = formatted_date.replace('-', '_')  # Replace hyphens with underscores to make it safe
        # Make sure the date is in the correct format (YYYY-MM-DD)
        datetime.strptime(formatted_date, "%Y_%m_%d")  # This will raise an error if the format is incorrect
    except ValueError:
        return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."})

    # Use this formatted date along with the class and section to create the table
    try:
        table_name = f"attendance_{c}_{s}_{formatted_date}"
        
        # Log the table name to confirm it's correctly formatted
        print(f"Table Name: {table_name}")  # For debugging
        
        # Execute the table creation
        query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            status TEXT
        );
        """
        
        with connection.cursor() as cursor:
            cursor.execute(query)

        return JsonResponse({'status': 'success', 'message': f'Table {table_name} created successfully.'})
    except Exception as e:
        return JsonResponse({"error": f"Error creating table: {str(e)}"})
