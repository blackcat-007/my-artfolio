
  <h1>🎨 My Artfolio</h1>

  <p>Welcome to <strong>My Artfolio</strong>, a personal portfolio website where I showcase my artistic creations — from <strong>photography</strong> and <strong>video editing</strong> to <strong>digital art</strong>. Built using <code>HTML</code>, <code>CSS</code>, and <code>Django</code>, this platform allows users to browse my work and even express their interest via a contact form.</p>

  <p>🔗 <a href="https://github.com/blackcat-007/my-artfolio" target="_blank">GitHub Repository</a></p>

  <div class="section">
    <h2>🌟 Features</h2>
    <ul>
      <li>🖼️ Display gallery of <strong>artworks, photographs, and video projects</strong></li>
      <li>🧑‍💻 Built with clean HTML, CSS, and Django templates</li>
      <li>📬 <strong>Contact Form</strong> with auto-email functionality</li>
      <li>✉️ On form submission, users receive an automatic email response</li>
      <li>🗂️ Well-structured backend with Django's MVC pattern</li>
      <li>⚙️ Easily maintainable and extendable for future growth</li>
    </ul>
  </div>

  <div class="section">
    <h2>🧰 Tech Stack</h2>
    <table class="table">
      <thead>
        <tr>
          <th>Layer</th>
          <th>Technology Used</th>
          <th>Purpose</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Frontend</td>
          <td>HTML, CSS</td>
          <td>For static layout and styling</td>
        </tr>
        <tr>
          <td>Backend</td>
          <td>Django</td>
          <td>Handles form, logic, and rendering</td>
        </tr>
        <tr>
          <td>Email</td>
          <td>smtplib or Django Email Backend</td>
          <td>Sends emails on form submission</td>
        </tr>
        <tr>
          <td>Server Logic</td>
          <td>views.py, forms.py, urls.py</td>
          <td>Request handling and routing</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="section">
    <h2>📁 Project Structure</h2>
    <pre>
my-artfolio/
├── portfolio/
│   ├── templates/
│   │   ├── index.html             # Home page
│   │   ├── gallery.html           # Gallery of artworks/videos
│   │   └── contact.html           # Contact form page
│   ├── static/                    # CSS, images, videos
│   ├── views.py                   # Handles logic and form
│   ├── forms.py                   # Contact form definition
│   └── urls.py                    # URL routing
├── my_artfolio/                   # Django settings
├── manage.py
└── README.html
    </pre>
  </div>

  <div class="section">
    <h2>🛠️ Setup Instructions</h2>
    <ol>
      <li><strong>Clone the Repository:</strong><br>
        <code>git clone https://github.com/blackcat-007/my-artfolio.git</code><br>
        <code>cd my-artfolio</code>
      </li>
      <li><strong>Create and Activate Virtual Environment:</strong><br>
        <code>python -m venv env</code><br>
        <code>source env/bin/activate</code> (on Windows: <code>env\Scripts\activate</code>)
      </li>
      <li><strong>Install Dependencies:</strong><br>
        <code>pip install -r requirements.txt</code>
      </li>
      <li><strong>Run the Server:</strong><br>
        <code>python manage.py runserver</code>
      </li>
    </ol>
    <p>Then open your browser and go to: <code>http://127.0.0.1:8000</code></p>
  </div>

  <div class="section">
    <h2>📬 Email Automation (How It Works)</h2>
    <div class="highlight">
      When a visitor submits the contact form:<br>
      1. Data is sent to the server<br>
      2. An auto-response email is sent to the visitor<br>
      3. Optional: You (the admin) get notified too
    </div>
  </div>

  <div class="section">
    <h2>📸 Gallery Highlights</h2>
    <ul>
      <li>🎨 Abstract Sketches</li>
      <li>📷 Portrait & Landscape Photography</li>
      <li>🎬 Video Editing & Motion Projects</li>
    </ul>
  </div>

  <div class="section">
    <h2>📌 Future Plans</h2>
    <ul>
      <li>🌗 Dark Mode toggle</li>
      <li>🖌️ Filter-based artwork browsing</li>
      <li>📊 Visitor analytics dashboard</li>
      <li>🔐 Admin login for backend uploads</li>
      <li>🌍 Deploy on Heroku / Render / Vercel</li>
    </ul>
  </div>

  <div class="section">
    <h2>🙋‍♂️ Developed By</h2>
    <p><strong>Shubho (blackcat-007)</strong><br>
      🎭 Artist | 👨‍💻 Developer | 🎬 Visual Creator<br>
      📫 <a href="https://github.com/blackcat-007" target="_blank">GitHub Profile</a>
    </p>
  </div>

  <div class="section">
    <h2>📄 License</h2>
    <p>This project is available in public domain</p>
  </div>

  <blockquote>
    🎨 “Art enables us to find ourselves and lose ourselves at the same time.” – Thomas Merton
  </blockquote>

