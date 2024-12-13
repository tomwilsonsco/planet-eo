from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from io import BytesIO


# Can plot the thumbnails, but note these are not georeferenced
class PreviewPlot:
    """Plot thumbnail image overviews from image search result dataframe."""

    def __init__(self, search_df):
        """Initialise PreviewPlot"""
        self.df = search_df
        self.current_row = 0
        self.max_row = search_df.shape[0] - 1
        self.current_link = None
        self.current_title = None

    def thumbnail_plot(self, image_data):
        """Request response to plot"""
        img = Image.open(BytesIO(image_data))
        img = img.convert("RGB")
        img = ImageOps.autocontrast(img)
        plt.figure(figsize=(20, 20))
        plt.imshow(img)
        plt.axis("off")
        plt.title(f"Image ID: {self.current_title}", fontsize=24, color="red")
        plt.show()

    def update_link(self):
        """Get current row thumbnail link"""
        self.current_link = self.df.iloc[self.current_row]["thumbnail_link"]

    def update_title(self):
        """Get current row image id for plot title"""
        self.current_title = self.df.iloc[self.current_row]["id"]

    async def fetch_thumbnail(self, thumbnail_url):
        """Thumbnail URL request"""
        async with Session() as sess:
            response = await sess.request("GET", url=f"{thumbnail_url}?width=2048")
            return response._http_response.content

    async def view_thumbnail(self):
        """Overall method to view a thumbnail and increment current row"""
        print(f"plotting thumbnail {self.current_row + 1} of {self.max_row + 1}..")
        self.update_link()
        self.update_title()
        print(self.current_title)
        image_data = await self.fetch_thumbnail(self.current_link)
        self.thumbnail_plot(image_data)
        if self.current_row < self.max_row:
            self.current_row += 1
        else:
            self.current_row = 0
