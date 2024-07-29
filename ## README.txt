## README



Overview
This project analyzes order data from an online store to:
* Calculate monthly revenue.
* Calculate product-wise revenue.
* Calculate customer-wise revenue.
* Identify top 10 customers by revenue.

The project uses Python, pandas, and unittest for testing. The application is Dockerized for easy deployment and isolation.

Prerequisites
* Python 3.9+
* Docker
Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/order_analysis.git
   ```
2. Install dependencies:
   ```bash
   cd order_analysis
   pip install -r requirements.txt
   ```
3. Prepare data:
   Place your order data in a CSV file named `orders.csv` with the specified columns:
   * order_id
   * customer_id
   * order_date
   * product_id
   * product_name
   * product_price
   * quantity

Running the Application
1. Build Docker images:
   ```bash
   docker build -t order_analysis .
   docker build -t order_analysis_test .
   ```
2. Run the task service:
   ```bash
   docker run -v /path/to/your/data:/app/orders.csv order_analysis
   ```
   Replace `/path/to/your/data` with the actual path to your `orders.csv` file.
3. Run the test service:
   ```bash
   docker run order_analysis_test
   ```
Running the Application
1. Build Docker images:
   ```bash
   docker build -t order_analysis .
   docker build -t order_analysis_test .
   ```
2. **Run the task service:**
   ```bash
   docker run -v /path/to/your/data:/app/orders.csv order_analysis
   ```
   Replace `/path/to/your/data` with the actual path to your `orders.csv` file.
3. **Run the test service:**
   ```bash
   docker run order_analysis_test
   ```




