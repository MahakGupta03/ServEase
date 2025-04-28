# ServEase - An Online Marketplace for Local Services
## Features
- **Service Provider Registration:** Providers can register using a unique ID (e.g., Aadhaar card) to verify their authenticity.
- **Service Categorization:** Providers list their services under specific domains for easy navigation.
- **Customer Service Requests:** Customers can browse and select service providers based on their needs.
- **E-Bidding System:** Providers can bid on service requests within a customer-defined timeframe, allowing customers to compare profiles and bids to choose the most suitable provider.

## Technologies Used
- **Backend:** Python, Django
- **Database:** MongoDB
- **Frontend:** HTML, CSS, JavaScript, Bootstrap

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/MahakGupta03/Minor-Project.git
   cd Minor-Project

2. **Set Up a Virtual Environment:**
      ```sh
      python3 -m venv venv
      venv\Scripts\activate   # On Mac, use `source venv/bin/activate`

3. **Install Dependencies:**
      ```sh
      pip install -r requirements.txt

4. **Apply Migrations:**
   ```sh
      python manage.py makemigrations
      python manage.py migrate

5. **Run the Development Server:**
      ```sh
      python manage.py runserver
Access the application at http://127.0.0.1:8000/.

## Usage
- **For Service Providers:**
  - Register using a valid unique ID.
  - List your services under the appropriate categories.
  - Monitor and bid on available service requests.

- **For Customers:**

  - Browse service categories to find providers.
  - Post service requests detailing your requirements.
  - Review bids and provider profiles to make informed decisions.
     
