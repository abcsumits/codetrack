CodeTrack
http://bit.ly/code-track

Overview:
CodeTrack is a comprehensive web application designed to streamline the process of tracking and managing competitive programming progress and achievements. This project involved the development of a feature-rich platform that enables users to monitor their ratings and rankings on popular coding competition websites such as Codeforces, LeetCode, and CodeChef. By integrating user authentication and verification, email communication, data scraping techniques, and the Codeforces API, CodeTrack offers a seamless experience for competitive programmers seeking to monitor their performance.

Key Features:

Multi-Platform Ratings Tracking: CodeTrack allows users to monitor their ratings and rankings on three prominent competitive programming platforms—Codeforces, LeetCode, and CodeChef. Users can view their progress and compare their performance across these platforms from a single dashboard.

Token-Based User Verification: To ensure the accuracy and security of user data, CodeTrack implements a token-based verification system. Users are required to verify their accounts on each platform by changing their username to a unique token generated by CodeTrack. This token is then used for scraping their data securely.

Codeforces API Integration: CodeTrack utilizes the Codeforces API to access real-time information, including contest details, problem sets, and user submissions. This integration enhances the user experience by providing up-to-date Codeforces data directly within the platform.

AWS EC2 Hosting with Gunicorn: CodeTrack is hosted on Amazon Web Services (AWS) Elastic Compute Cloud (EC2) instances, ensuring high availability and scalability. Gunicorn, a WSGI HTTP server, is used for efficient and reliable deployment of the Django application.

Data Collection with BeautifulSoup: BeautifulSoup, a Python library for web scraping, is employed to extract data from the supported coding competition platforms. It retrieves user-specific information such as rating changes, contest participation history, and more.

Institute Leaderboard: CodeTrack offers an institute leaderboard feature, allowing users to compare their performance with fellow students or colleagues from the same educational institution. This fosters healthy competition and motivates users to improve their coding skills.

Following and Follower Leaderboards: Users can follow and be followed by others, creating a social aspect within the platform. CodeTrack maintains leaderboards for both followers and followees, making it easier to track the progress of friends and rivals.

Password Reset: In the event of a forgotten password, CodeTrack provides a secure password reset functionality. Users receive email notifications with a link to reset their passwords, ensuring account security and accessibility.

Email-Based User Verification: CodeTrack leverages email verification to confirm the authenticity of user accounts. Users receive a verification link via email during registration, enhancing the security of the platform.

For more details and to experience CodeTrack, please visit the project website: CodeTrack Website.

Technologies Used:

Django: A powerful Python web framework used to build the backend of CodeTrack.
BeautifulSoup: A Python library for web scraping used to collect data from coding competition platforms.
Codeforces API: Provides real-time data from the Codeforces platform.
AWS EC2: Provides scalable and reliable hosting for the application.
Gunicorn: A WSGI HTTP server used for deploying the Django application.
HTML/CSS: Frontend components and styling.
Email services for user verification and password reset.
CodeTrack is a testament to your skills in web development, data scraping, and system architecture. It offers a valuable tool for competitive programmers to track their progress and engage with a community of like-minded individuals. To explore the project further, please visit the CodeTrack website. Your contributions to this project demonstrate your ability to design and implement complex web applications with a focus on user experience and data security.
