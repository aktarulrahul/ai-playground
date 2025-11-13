import express from "express";
import dotenv from "dotenv";
import router from "./routers";
dotenv.config();

const app = express();
app.use(express.json());
app.use(router);

const port = process.env.PORT || 5001;

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
