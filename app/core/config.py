from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Configuración global del proyecto.
    Lee y valida las variables desde el archivo .env.
    Si falta una variable o tiene el tipo incorrecto, Pydantic avisa antes
    de que la aplicación arranque.
    """
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str = ""  # Vacío por defecto (Mi XAMPP no tiene contraseña)

    
    @property
    def DATABASE_URL(self) -> str:
        # Arma la URL automáticamente juntando las partes de las variables de .env
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    # Le decimos a Pydantic que busque estas variables en el archivo .env
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8"
    )

# Instanciamos la configuración para poder importarla en otros archivos
settings = Settings()