// MOCK API (no backend needed)
export const analyzeSprint = async (distance, time) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const speed = (distance / time).toFixed(2);
      resolve({ speed });
    }, 500);
  });
};
