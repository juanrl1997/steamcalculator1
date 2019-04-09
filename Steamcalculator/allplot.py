def allplot(Pvalue,Tvalue,vvalue,hvalue,svalue):
    import plots
    from io import BytesIO
    import base64
    import matplotlib.pyplot as plt
    import numpy as np

# plot 1
    plots.Pvplot(Pvalue,vvalue)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
# plot 2
    plots.Phplot(Pvalue,hvalue)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic2 = base64.b64encode(image_png)
    graphic2 = graphic2.decode('utf-8')
# plot 3
    plots.Tsplot(Tvalue,svalue)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic3 = base64.b64encode(image_png)
    graphic3 = graphic3.decode('utf-8')

# plot 4
    plots.Hsplot(hvalue,svalue)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic4 = base64.b64encode(image_png)
    graphic4 = graphic4.decode('utf-8')

    return[graphic,graphic2, graphic3, graphic4]
