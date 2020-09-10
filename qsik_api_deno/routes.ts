import { Router } from "https://deno.land/x/oak/mod.ts";
import { home, createParty, getParties, getParty } from "./controller.ts";

const router = new Router();
router.get("/", home)
  .post("/api/createParty", createParty)
  .get("/api/parties", getParties)
  .get("/api/party/:id", getParty);

export default router;
