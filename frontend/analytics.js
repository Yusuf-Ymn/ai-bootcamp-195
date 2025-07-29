// analytics.js
// 1) ESM modüllerini import ediyoruz:
import {
  Chart,
  registerables,
} from "https://cdn.jsdelivr.net/npm/chart.js@4.3.0/dist/chart.esm.js";
import {
  MatrixController,
  MatrixElement,
} from "https://cdn.jsdelivr.net/npm/chartjs-chart-matrix@1.1.0/dist/chartjs-chart-matrix.esm.js";
import ChartDataLabels from "https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.2.0/dist/chartjs-plugin-datalabels.esm.js";

// 2) Chart.js’e hem tüm "registerables" hem de matrix eklentisi + datalabels'ı ekliyoruz
Chart.register(
  ...registerables,
  MatrixController,
  MatrixElement,
  ChartDataLabels
);

console.log("📊 analytics.js (ESM) loaded");

document.addEventListener("DOMContentLoaded", async () => {
  try {
    // 3) Backend'ten korelasyon matrisini çek
    const res = await fetch("/analytics/corr-matrix");
    if (!res.ok) throw new Error(`API error: ${res.status}`);
    const { labels, matrix } = await res.json();

    // 4) Chart.js data formatına dönüştür
    const data = [];
    for (let i = 0; i < labels.length; i++) {
      for (let j = 0; j < labels.length; j++) {
        data.push({ x: j, y: i, v: matrix[i][j] });
      }
    }

    // 5) Isı haritasını çiz
    const ctx = document.getElementById("corr-heatmap").getContext("2d");
    new Chart(ctx, {
      type: "matrix",
      data: {
        datasets: [
          {
            label: "Korelasyon Matrisi",
            data,
            backgroundColor: ({ dataset, dataIndex }) => {
              const v = dataset.data[dataIndex].v;
              const r = Math.round((1 - v) * 255);
              const b = Math.round((1 + v) * 255);
              return `rgba(${r},0,${b},0.8)`;
            },
            datalabels: {
              anchor: "center",
              formatter: (ctx) => ctx.dataset.data[ctx.dataIndex].v.toFixed(2),
              color: "#000",
              font: { size: 10 },
            },
            width: ({ chart }) =>
              chart.chartArea ? chart.chartArea.width / labels.length - 2 : 0,
            height: ({ chart }) =>
              chart.chartArea ? chart.chartArea.height / labels.length - 2 : 0,
          },
        ],
      },
      options: {
        scales: {
          x: {
            type: "category",
            labels,
            offset: true,
            grid: { display: false },
            ticks: { maxRotation: 45, minRotation: 45 },
          },
          y: {
            type: "category",
            labels: [...labels].reverse(),
            offset: true,
            grid: { display: false },
          },
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              title: () => "",
              label: (ctx) => {
                const { x, y, v } = ctx.dataset.data[ctx.dataIndex];
                return `${labels[y]} × ${labels[x]}: ${v.toFixed(2)}`;
              },
            },
          },
          datalabels: { display: true },
        },
        layout: { padding: { top: 10, bottom: 10 } },
      },
    });

    console.log("✅ Chart rendered");
  } catch (err) {
    console.error("❌ Chart çizilirken hata:", err);
    alert("Grafik yüklenemedi, konsolu kontrol edin.");
  }
});
