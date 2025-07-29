# app/routes/analytics.py
import pandas as pd
import traceback
from fastapi import APIRouter, HTTPException
from sqlalchemy import inspect
from app.core.database import engine

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/inspect-tables")
def inspect_tables():
    insp = inspect(engine)
    return {"tables": insp.get_table_names()}

@router.get("/corr-matrix")
def get_corr_matrix():
    try:
        # Tabloyu oku
        df_sum = pd.read_sql_table("daily_summaries", con=engine)
        df_met = pd.read_sql_table("daily_metrics",   con=engine)

        if df_sum.empty or df_met.empty:
            raise HTTPException(status_code=404, detail="Henüz veri yok")

        # Merge
        df = df_sum.merge(df_met, on=["user_id", "date"], how="inner")

        # Duygu skoruna çevir
        mapping = {"Üzgün":1, "Stresli":2, "Nötr":3, "Mutlu":4, "Keyifli":5}
        df["emotion_score"] = df["emotion"].map(mapping)
        if df["emotion_score"].isnull().any():
            df["emotion_score"], _ = pd.factorize(df["emotion"])

        # Korelasyon matrisi için sütunlar
        cols = [
          "emotion_score",
          "sleep_hours",
          "water_glasses",
          "screen_time_hours",
          "coffee_cups",
          "exercise_minutes"
        ]
        sub = df[cols].dropna()  # eksikleri at

        # Pearson korelasyonu
        corr = sub.corr(method="pearson")

        # **Burada NaN’ları 0 ile dolduruyoruz**
        corr = corr.fillna(0.0)

        return {
          "labels": corr.columns.tolist(),
          "matrix": corr.values.tolist()
        }

    except HTTPException:
        # Özel hata kodlarıyla fırlatılanları olduğu gibi ilet
        raise
    except Exception as e:
        # Konsola full traceback’i bas
        traceback.print_exc()
        # HTTP 500 olarak kullanıcıya sadece mesajı dön
        raise HTTPException(status_code=500, detail=str(e))
