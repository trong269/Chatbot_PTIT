<template>
  <div class="typing-dots">
    <div class="dot"></div>
    <div class="dot"></div>
    <div class="dot"></div>
  </div>
</template>

<style lang="scss" scoped>
@keyframes darker {
  0% {
    opacity: 0.5;
  }
  50% {
    opacity: 0.2;
  }
  100% {
    opacity: 1;
  }
}

.typing-dots {
  display: flex;
  gap: 6px;
  padding-top: 10px;

  .dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: var(--p-gray-700);
    animation: darker 1s infinite;

    &:nth-child(2) {
      animation-delay: 0.1s;
    }

    &:nth-child(3) {
      animation-delay: 0.2s;
    }
  }
}
</style>
