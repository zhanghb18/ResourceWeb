<template>
    <div class="profile-wrapper">
      <div class="profile">
        <div class="avatar">
          <img src="https://placekitten.com/200/200" alt="avatar" />
        </div>
        <div class="info">
          <h2>{{ username }}</h2>
          <p>{{ bio }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ProfilePage",
    data() {
      return {
        username: "John Doe",
        bio: "I love coding and playing video games",
      };
    },
  };
  </script>
  
  <style>
  /* 样式表 */
  .profile-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f5f5f5;
  }
  
  .profile {
    position: relative;
    width: 400px;
    height: 400px;
    background-color: #fff;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  
  .avatar {
    position: absolute;
    top: -100px;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    overflow: hidden;
  }
  
  .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .info {
    margin-top: 80px;
    text-align: center;
  }
  
  .info h2 {
    margin: 0;
    font-size: 24px;
  }
  
  .info p {
    margin: 8px 0 0;
    font-size: 16px;
  }
  </style>