<template>
  <div class="d-flex flex-column min-vh-100">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg fixed-top">
      <div class="container">
        <router-link class="navbar-brand neon-text" to="/Home">
          <span class="flicker-slow">ਅਰਸ਼ਦੀਪ</span>
          <span class="flicker-fast">ਸਿੰਘ</span>
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMenu">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navMenu">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link class="nav-link neon-hover" to="/Home">
                <span class="nav-glow">Home</span>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link neon-hover" to="/About">
                <span class="nav-glow">About</span>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link neon-hover" to="/Projects">
                <span class="nav-glow">Projects</span>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link neon-hover" to="/Contact">
                <span class="nav-glow">Contact</span>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link neon-hover" to="/Resume">
                <span class="nav-glow">Resume</span>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link neon-hover"
                to="/Members">
                <span class="nav-glow">Members</span>
              </router-link>
            </li>

          </ul>
        </div>
      </div>
    </nav>

    <!-- Main content -->
    <main class="flex-grow-1 mt-5 pt-3">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="site-footer py-4 bg-light text-center mt-auto">
      <div class="container">
        <div class="footer-content">
          <p class="copyright mb-3">&copy; 2025 Arshdeep Singh. All rights reserved.</p>

          <div class="social-links">
            <a href="https://github.com/sengh2001" target="_blank" rel="noopener noreferrer" class="social-link">
              <i class="bi bi-github"></i>
              <span class="visually-hidden">GitHub</span>
            </a>
            <a href="https://www.linkedin.com/in/arshdeep-singh-bhankhar/" target="_blank" rel="noopener noreferrer"
              class="social-link">
              <i class="bi bi-linkedin"></i>
              <span class="visually-hidden">LinkedIn</span>
            </a>
            <a href="https://twitter.com/arshdeep" target="_blank" rel="noopener noreferrer" class="social-link">
              <i class="bi bi-twitter-x"></i>
              <span class="visually-hidden">Twitter</span>
            </a>
            <a href="mailto:arsh.thapar24@gmail.com" class="social-link">
              <i class="bi bi-envelope-fill"></i>
              <span class="visually-hidden">Email</span>
            </a>
          </div>
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup>
// No script needed
</script>

<style scoped>
main {
  padding-top: 56px;
}

.site-footer {
  border-top: 1px solid rgba(0, 0, 0, 0.1);
}

.footer-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.copyright {
  color: #6c757d;
  font-size: 0.9rem;
}

.social-links {
  display: flex;
  gap: 1.25rem;
}

.social-link {
  color: #495057;
  font-size: 1.25rem;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
}

.social-link:hover {
  color: #0d6efd;
  transform: translateY(-2px);
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.navbar {
  background: rgba(10, 10, 15, 0.8) !important;
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(100, 255, 255, 0.1);
  box-shadow: 0 0 10px rgba(100, 255, 255, 0.2);
}

.neon-text {
  font-family: 'Rajdhani', sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #fff;
  text-shadow:
    0 0 5px #fff,
    0 0 10px #fff,
    0 0 20px #0ff,
    0 0 40px #0ff;
}

.flicker-slow {
  animation: flicker 3s linear infinite;
}

.flicker-fast {
  animation: flicker 1s linear infinite;
}

@keyframes flicker {

  0%,
  19.999%,
  22%,
  62.999%,
  64%,
  64.999%,
  70%,
  100% {
    opacity: 1;
    text-shadow:
      0 0 5px #fff,
      0 0 10px #fff,
      0 0 20px #0ff,
      0 0 40px #0ff;
  }

  20%,
  21.999%,
  63%,
  63.999%,
  65%,
  69.999% {
    opacity: 0.5;
    text-shadow: none;
  }
}

.nav-glow {
  position: relative;
}

.nav-glow::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #0ff;
  z-index: -1;
  opacity: 0;
  transform: scale(0.8);
  transition: all 0.3s ease;
}

.neon-hover:hover .nav-glow::before {
  opacity: 0.1;
  transform: scale(1.1);
  box-shadow: 0 0 15px #0ff;
}

.nav-link {
  color: rgba(255, 255, 255, 0.8) !important;
  margin: 0 10px;
  position: relative;
  transition: all 0.3s ease;
}

.nav-link:hover {
  color: #fff !important;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: #0ff;
  transition: width 0.3s ease;
}

.nav-link:hover::after,
.router-link-exact-active::after {
  width: 100%;
}

.router-link-exact-active {
  color: #fff !important;
  text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
}

.navbar-toggler {
  border-color: rgba(0, 255, 255, 0.5);
}

.navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%280, 255, 255, 0.8%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}
</style>