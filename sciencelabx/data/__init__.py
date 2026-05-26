import pandas as pd

class Data:

    def __init__(self, data: pd.DataFrame, show_info: bool = True):
        self.data = data
        if data is not None:
            self._numerical_cols = data.select_dtypes(include=["int", "float"]).columns.tolist()
            self._categorical_cols = data.select_dtypes(include=["object"]).columns.tolist()
        else:
            print("No data provided")

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


    def summary_data(
            df,
            metric: "list | str" = ["mean", "mode", "median", "std", "var", "min", "max", "quantiles", "count", "NaN"],
            return_str: bool = True,
            return_metrics: bool = False,
            decimals: int = 2,
    ):
        # Variables numericas y categoricas
        columnas = df.columns
        ## Filas y columnas
        n_columnas = df.shape[1]
        n_filas = df.shape[0]
        ## Diccionario de Metricas
        dic_metricas = {}

        ## Intentar transformar categoricas a numericas si es el caso
        for col in columnas:
            if df[col].dtype == "object":
                try:
                    df[col] = df[col].astype("float64")
                except:
                    pass

        numericas = df.select_dtypes(include=["number"]).columns
        categoricas = df.select_dtypes(include=["object"]).columns

        # Media
        if "mean" in metric:
            mean_variables = []

            for col in numericas:

                ## Media por columna
                mean = float(round(df[col].sum() / len(df[col]), decimals))

                mean_variables.append((col, mean))

            dic_metricas["mean"] = mean_variables
        
        # Moda
        if "mode" in metric:
            mode_variables = []

            for col in columnas:
                if col in numericas:

                    ## Moda por columna
                    mode = df[col].value_counts().sort_values(ascending=False).iloc[ : min(n_columnas, n_filas)].to_dict()

                else:
                    mode = df[col].mode().to_dict()

                mode_variables.append((col, mode))

            dic_metricas["mode"] = mode_variables

        # Mediana
        if "median" in metric:
            median_variables = []
            
            for col in numericas:
                # Sort once and drop NaNs
                sorted_col = df[col].dropna().sort_values().reset_index(drop=True)
                n = len(sorted_col)
                
                if n == 0:
                    median = 0 
                elif n % 2 != 0:
                    median = sorted_col.iloc[n // 2]
                else:
                    # Even: average of the two middle elements
                    low = sorted_col.iloc[(n // 2) - 1]
                    high = sorted_col.iloc[n // 2]
                    median = (low + high) / 2
                    
                median_variables.append((col, round(float(median), decimals)))

            dic_metricas["median"] = median_variables

        # Varianza
        if "var" in metric:
            var_variables = []
            
            for col in numericas:
                col_data = df[col].dropna()
                media = col_data.mean()
                
                varianza = ((col_data - media) ** 2).sum() / (len(col_data) - 1)
                
                var_variables.append((col, float(round(varianza, decimals))))

            dic_metricas["var"] = var_variables

        # Desviacion Estandar
        if "std" in metric:
            std_variables = []

            for col in numericas:
                col_data = df[col].dropna()
                media = col_data.mean()

                desviacion = ((col_data - media) ** 2).sum() / (len(col_data) - 1)

                std_variables.append((col, float(round(desviacion ** 0.5, decimals))))

            dic_metricas["std"] = std_variables

        # Minimo y Maximo
        if "min" in metric:
            min_variables = []

            for col in numericas:
                min_variables.append((col, float(round(df[col].min(), decimals))))

            dic_metricas["min"] = min_variables

        if "max" in metric:
            max_variables = []

            for col in numericas:
                max_variables.append((col, float(round(df[col].max(), decimals))))

            dic_metricas["max"] = max_variables

        # Cuantiles
        if "quantiles" in metric:
            quantiles_variables = []

            for col in numericas:
                quantiles_variables.append((col, df[col].quantile([0.25, 0.5, 0.75]).to_dict()))

            dic_metricas["quantiles"] = quantiles_variables
            
        # Conteo
        if "count" in metric:
            count_variables = []

            for col in columnas:
                if col in numericas:
                    count_variables.append((col, int(df[col].dropna().count())))
                else:
                    if df[col].dropna().count() > 0:
                        count_variables.append((col, int(df[col].dropna().count())))

            dic_metricas["count"] = count_variables

        if "NaN" in metric:
            nan_variables = []

            for col in columnas:
                nan_variables.append((col, int(df[col].isna().sum())))

            dic_metricas["NaN"] = nan_variables

        # Formato de salida
        if return_str:
            print("*" * 120)
            print("\n                   RESUMEN DEL DATASET ~ METODO DESCRIBE                              (Columnas, Filas): ({}, {})".format(n_columnas, n_filas))
            print("*" * 120)
            print("INFORMACION RELEVANTE:\n")
            print(f"Columnas: {n_columnas} - Filas: {n_filas}\n")
            print(f"Variables Numericas: {len(numericas)}")
            for var in df[numericas].columns:
                print(f"\t{var}: {df[var].dtype}")
            print(f"Variables Categoricas: {len(categoricas)}")
            for var in df[categoricas].columns:
                print(f"\t{var}: {df[var].dtype}")
            print("*" * 120)
            print("\n")
            for key in dic_metricas.keys():
                print(f"{key}:")
                for item in dic_metricas[key]:
                    print(f"\t{item[0]}: {item[1]}")
            print("\n")
            print("*"*120)

        if return_metrics:
            return dic_metricas



