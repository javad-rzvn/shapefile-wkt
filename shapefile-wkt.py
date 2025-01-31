import marimo

__generated_with = "0.10.18"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import geopandas as gpd
    return gpd, mo


@app.cell
def _(mo):
    shapefiles = mo.ui.file(filetypes=[".zip"], kind="area", multiple=True)
    shapefiles
    return (shapefiles,)


@app.cell
def _(gpd, shapefiles):
    shapefile_df = {}
    if len(shapefiles.value) > 0:
        print(shapefiles.value)
        for item in shapefiles.value:
            df = gpd.read_file(item.contents)
            shapefile_df.update({item.name: df})

    return df, item, shapefile_df


@app.cell
def _(shapefile_df):
    len(shapefile_df)
    return


@app.cell
def _(mo, shapefile_df, shapefiles):
    a = True
    if len(shapefiles.value) > 0:
        preview_tabs = {file_name:mo.ui.table(file_content, page_size=5) for file_name, file_content in shapefile_df.items()}
    else:
        preview_tabs = {"Error": "Empty"}

    mo.ui.tabs(preview_tabs)
    return a, preview_tabs


@app.cell
def _():
    # shapefile_columns = {}
    # for fname, fcontent in shapefile_df.items():
    #     file_cols = {
    #         fname: {
    #             col_name: mo.ui.text(value=col_name) for col_name in fcontent.columns
    #         }
    #     }
    #     shapefile_columns.update(file_cols)

    # mo.ui.tabs(shapefile_columns)
    return


@app.cell
def _():
    # te = shapefile_columns["plain.zip"]["OBJECTID_1"]
    # print(te.value)
    return


if __name__ == "__main__":
    app.run()
