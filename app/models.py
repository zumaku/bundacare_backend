from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)  # PostgreSQL otomatis menangani autoincrement
    username = Column(String, unique=True, nullable=False)
    nik = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    nutritions = relationship("Nutrition", back_populates="user")

class Nutrition(Base):
    __tablename__ = "nutritions"

    id = Column(Integer, primary_key=True)  # PostgreSQL otomatis menangani autoincrement
    nama_makanan = Column(String, nullable=False)
    gambar = Column(String)
    kalori = Column(Integer, nullable=False)
    protein = Column(Integer, nullable=False)
    karbo = Column(Integer, nullable=False)
    lemak = Column(Integer, nullable=False)
    judul_deskripsi = Column(String, nullable=False)
    isi_deskripsi = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="nutritions")
