<template>
  <div class="app">
    <header class="topbar">
      <div>
        <h1>JTA - DummyJSON Dashboard</h1>
      </div>

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/users">Users</RouterLink>
        <RouterLink to="/products">Products</RouterLink>
      </nav>
    </header>

    <main class="page">
      <RouterView />
    </main>
  </div>
</template>


<style scoped>
.app {
  min-height: 100vh;
}

.topbar {
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.topbar h1 {
  margin: 0;
}

nav {
  display: flex;
  gap: 1rem;
}

nav a {
  color: var(--color-text);
  text-decoration: none;
  font-weight: 600;
}

nav a.router-link-active {
  color: blue;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

.page {
  padding: 2rem;
}
</style>
