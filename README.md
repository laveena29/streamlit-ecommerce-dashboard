# streamlit-ecommerce-dashboard
This project is a data visualization dashboard built using Streamlit to analyze fake e-commerce transaction data.<br>

The dashboard allows users to view several metrics and insights, including:<br>
Daily Profit/Loss: A graph that indicates daily profit/loss fluctuations.<br>
Most Popular Products: A bar chart showing the number of orders received or revenue generated in relation to the most popular products.
Filtering: The data can be filtered by product, category, or any other metric.<br>
Potential Fraudulent Orders:A fraudulent order is indicated by using a heuristic in the form of unusual discount orders or low price orders. This project has used fake data for simulating e-commerce transactions. <br>

Steps to Execute:<br>
Step 1: Start by generating the csv which will be used as an input for the main.py file. This step includes installing all the libraries used in the  fakeData.py file , a csv file is generated which should be saved in the same folder as where your main file be.<br>
Step2: Save your main file in the same folder as your csv file and the fakeData.py file run it on your preferred environment.<br>
Step3: Install all the libraries using your command prompt.<br>
Step4: After the code is successfully complied it will redirect you to your default browser and your streamlit application will be launched.<br>

//Some Problems I faced:<br>
->I was using VS code to run my code , where I faced issue with the selctionOfterminal so I used the VS code inbuilt terminal to execute my code through the following steps:<br>
1) cd "path to my main.py file"<br>
2)  streamlit run main.py <br>
This worked for me and I was redirected to my browser where I could see my application.<br>
