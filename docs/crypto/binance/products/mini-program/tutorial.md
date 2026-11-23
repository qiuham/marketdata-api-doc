---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/tutorial
api_type: Guide
updated_at: 2026-11-23 18:30:24.468415
---

# Tutorial: Create a weather app by mini program

# Crafting a Dynamic Weather Mini-Program from Scratch

This comprehensive tutorial offers a step-by-step guide to building a dynamic weather mini-program.

The aim is to create a multi-page program that leverages the Amap's weather API, displaying weather
conditions for a user-selected city.

## Setting the Project Foundation

Start by [following the guide to create your mini program](quick-start#generate-your-mini-program).

The result? A new project built within the current directory, following this directory structure:

```
📦demo-app
 ┣ 📂pages
 ┃ ┣ 📂index
 ┃ ┃ ┣ 📜index.bxml
 ┃ ┃ ┣ 📜index.bxss
 ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┗ 📜index.json
 ┃ ┗ 📂logs
 ┃ ┃ ┣ 📜logs.bxml
 ┃ ┃ ┣ 📜logs.bxss
 ┃ ┃ ┣ 📜logs.js
 ┃ ┃ ┗ 📜logs.json
 ┣ 📂utils
 ┃ ┗ 📜util.js
 ┣ 📜app.bxss
 ┣ 📜app.js
 ┣ 📜app.json
 ┗ 📜project.config.json
```

## Building the List Page

Next, update the file code as follows:

┣ 📂index ┃ ┣ 📜index.bxml ┃ ┣ 📜index.js

```html
<view className="page-container">
  <text className="h1">Cities List</text>
  <navigator className="list-item" url="/pages/detail/index?city=Beijing"> Beijing </navigator>
  <navigator className="list-item" url="/pages/detail/index?city=Shanghai"> Shanghai </navigator>
  <navigator className="list-item" url="/pages/detail/index?city=Guangzhou"> Guangzhou </navigator>
  <navigator className="list-item" url="/pages/detail/index?city=Shenzhen"> Shenzhen </navigator>
</view>
```

```js
Page({
  // Triggered when the page is brought to the foreground.
  onShow() {},
  // Triggered when the page is hidden in the background.
  onHide() {},
});
```

In the code above, we are using the view, text, and navigator components to layout our page. The
mini program is equipped with a large collection of built-in components you can learn more about
from [Components](framework/components).

Page components also provide several lifecycle hooks, like `onShow()` and `onHide()`. These two
callbacks are triggered when the mini program toggles between the foreground and background of the
app. Learn more about lifecycle from [LifeCycle](framework/lifecycle).

We are transitioning between pages using the navigator component, which uses a 'url' parameter to
route us to the detail page. You can learn about routing and parameter passing from
[Router](framework/router).

## Creating the Details Page

Start by creating a 'detail' folder within `pages`, and generating the required files:

```
📦pages
┣ 📂detail
┃ ┣ 📜index.bxml
┃ ┣ 📜index.bxss
┃ ┣ 📜index.js
┃ ┗ 📜index.json
```

Add this new page to `src/app.config.json`:

```json
{
  "entryPage": "pages/index/index",
  "pages": [
    "pages/index/index",
    "pages/detail/index" // <- Add this line
  ],
  "window": {
    "backgroundTextStyle": "light",
    "navigationBarBackgroundColor": "#fff",
    "navigationBarTitleText": "Title",
    "navigationBarTextStyle": "black"
  }
}
```

Now you can begin drafting the code for the details page. You can do this by making some adjustments
to: ┣ 📂detail ┃ ┣ 📜index.bxml ┃ ┣ 📜index.js

## Developing the Details Page

Let's get started by setting up the code for the details page. We will need to update the following:
┣ 📂detail ┃ ┣ 📜index.bxml ┃ ┣ 📜index.js

```HTML
<view className="page-container">
  <text className="h1">{{city}} Weather</text>
  <text className="text">Temperature: {{temperature}}°C</text>
  <text className="text">Description: {{weatherDescription}}</text>
</view>
```

```js
Page({
  // Variables defined here are observable and can be used in templates.
  data: {
    city: "",
    temperature: "",
    weatherDescription: "",
  },
  // Triggered when the page is loaded.
  onLoad(query) {
    this.setData({
      city: query.city,
    });
    this.updateWeather();
  },
  async updateWeather() {
    // Obtain and parse the weather data...
    const weatherData = await fetchWeatherData(this.data.city);
    this.setData({
      temperature: weatherData.temperature,
      weatherDescription: weatherData.description,
    });
  },
});
```

The `onLoad(query)` function in the above code will be triggered when the page loads. `query`
contains the parameters passed from the previous page, which we then access to grab the city value.
It is also worth noting the `fetchWeatherData(city)` function. This function fetches and parses the
weather data. However, the specifics of this action are not detailed here for simplicity.

## Conclusion

This tutorial has guided you through the process of creating a simple and dynamic weather
mini-program. If you followed along, congratulations on your new program! Not only did you learn the
basic development process, but we hope it also inspired you to explore more about mini-program
development, such as using APIs and working with real-time data. Happy coding!

---

# Tutorial: Create a weather app by mini program

# Crafting a Dynamic Weather Mini-Program from Scratch

This comprehensive tutorial offers a step-by-step guide to building a dynamic weather mini-program.

The aim is to create a multi-page program that leverages the Amap's weather API, displaying weather
conditions for a user-selected city.

## Setting the Project Foundation

Start by [following the guide to create your mini program](quick-start#generate-your-mini-program).

The result? A new project built within the current directory, following this directory structure:

```
📦demo-app
 ┣ 📂pages
 ┃ ┣ 📂index
 ┃ ┃ ┣ 📜index.bxml
 ┃ ┃ ┣ 📜index.bxss
 ┃ ┃ ┣ 📜index.js
 ┃ ┃ ┗ 📜index.json
 ┃ ┗ 📂logs
 ┃ ┃ ┣ 📜logs.bxml
 ┃ ┃ ┣ 📜logs.bxss
 ┃ ┃ ┣ 📜logs.js
 ┃ ┃ ┗ 📜logs.json
 ┣ 📂utils
 ┃ ┗ 📜util.js
 ┣ 📜app.bxss
 ┣ 📜app.js
 ┣ 📜app.json
 ┗ 📜project.config.json
```

## Building the List Page

Next, update the file code as follows:

┣ 📂index ┃ ┣ 📜index.bxml ┃ ┣ 📜index.js

```html
<view className="page-container">
  <text className="h1">Cities List</text>
  <navigator className="list-item" url="/pages/detail/index?city=Beijing"> Beijing </navigator>
  <navigator className="list-item" url="/pages/detail/index?city=Shanghai"> Shanghai </navigator>
  <navigator className="list-item" url="/pages/detail/index?city=Guangzhou"> Guangzhou </navigator>
  <navigator className="list-item" url="/pages/detail/index?city=Shenzhen"> Shenzhen </navigator>
</view>
```

```js
Page({
  // Triggered when the page is brought to the foreground.
  onShow() {},
  // Triggered when the page is hidden in the background.
  onHide() {},
});
```

In the code above, we are using the view, text, and navigator components to layout our page. The
mini program is equipped with a large collection of built-in components you can learn more about
from [Components](framework/components).

Page components also provide several lifecycle hooks, like `onShow()` and `onHide()`. These two
callbacks are triggered when the mini program toggles between the foreground and background of the
app. Learn more about lifecycle from [LifeCycle](framework/lifecycle).

We are transitioning between pages using the navigator component, which uses a 'url' parameter to
route us to the detail page. You can learn about routing and parameter passing from
[Router](framework/router).

## Creating the Details Page

Start by creating a 'detail' folder within `pages`, and generating the required files:

```
📦pages
┣ 📂detail
┃ ┣ 📜index.bxml
┃ ┣ 📜index.bxss
┃ ┣ 📜index.js
┃ ┗ 📜index.json
```

Add this new page to `src/app.config.json`:

```json
{
  "entryPage": "pages/index/index",
  "pages": [
    "pages/index/index",
    "pages/detail/index" // <- Add this line
  ],
  "window": {
    "backgroundTextStyle": "light",
    "navigationBarBackgroundColor": "#fff",
    "navigationBarTitleText": "Title",
    "navigationBarTextStyle": "black"
  }
}
```

Now you can begin drafting the code for the details page. You can do this by making some adjustments
to: ┣ 📂detail ┃ ┣ 📜index.bxml ┃ ┣ 📜index.js

## Developing the Details Page

Let's get started by setting up the code for the details page. We will need to update the following:
┣ 📂detail ┃ ┣ 📜index.bxml ┃ ┣ 📜index.js

```HTML
<view className="page-container">
  <text className="h1">{{city}} Weather</text>
  <text className="text">Temperature: {{temperature}}°C</text>
  <text className="text">Description: {{weatherDescription}}</text>
</view>
```

```js
Page({
  // Variables defined here are observable and can be used in templates.
  data: {
    city: "",
    temperature: "",
    weatherDescription: "",
  },
  // Triggered when the page is loaded.
  onLoad(query) {
    this.setData({
      city: query.city,
    });
    this.updateWeather();
  },
  async updateWeather() {
    // Obtain and parse the weather data...
    const weatherData = await fetchWeatherData(this.data.city);
    this.setData({
      temperature: weatherData.temperature,
      weatherDescription: weatherData.description,
    });
  },
});
```

The `onLoad(query)` function in the above code will be triggered when the page loads. `query`
contains the parameters passed from the previous page, which we then access to grab the city value.
It is also worth noting the `fetchWeatherData(city)` function. This function fetches and parses the
weather data. However, the specifics of this action are not detailed here for simplicity.

## Conclusion

This tutorial has guided you through the process of creating a simple and dynamic weather
mini-program. If you followed along, congratulations on your new program! Not only did you learn the
basic development process, but we hope it also inspired you to explore more about mini-program
development, such as using APIs and working with real-time data. Happy coding!