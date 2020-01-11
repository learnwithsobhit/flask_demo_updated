<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tasks List</h1>
        <h1>Assigned To: Elam</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.task-modal>Add Task</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Task</th>
              <th scope="col">Status</th>
              <th scope="col">Deadline</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in tasks" :key="index">
              <td>
                <li style="float:left;">
                <a class="text-link" href="#">
                {{ item.task }}
                </a>
                </li>
              </td>
              <td>{{ item.status }}</td>
              <td>{{ item.deadline }}</td>
              <!-- <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td> -->
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.task-update-modal
                          @click="editTask(item)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteTask(item)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addTaskModal"
            id="task-modal"
            title="Add a new Task"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-task-group"
                    label="task:"
                    label-for="form-task-input">
          <b-form-input id="form-task-input"
                        type="text"
                        v-model="addTaskForm.task"
                        required
                        placeholder="Enter Task">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-status-group"
                      label="Status:"
                      label-for="form-status-input">
            <b-form-input id="form-status-input"
                          type="text"
                          v-model="addTaskForm.status"
                          required
                          placeholder="Enter Status">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-deadline-group"
                      label="Deadline:"
                      label-for="form-deadline-input">
            <b-form-input id="form-deadline-input"
                          type="text"
                          v-model="addTaskForm.deadline"
                          required
                          placeholder="Enter Deadline">
            </b-form-input>
          </b-form-group>
        <!-- <b-form-group id="form-deadline-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group> -->
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editTaskModal"
            id="task-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-task-edit-group"
                    label="Task:"
                    label-for="form-task-edit-input">
          <b-form-input id="form-task-edit-input"
                        type="text"
                        v-model="editForm.task"
                        required
                        placeholder="Enter task">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-status-edit-group"
                      label="Status:"
                      label-for="form-status-edit-input">
            <b-form-input id="form-status-edit-input"
                          type="text"
                          v-model="editForm.status"
                          required
                          placeholder="Enter status">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-deadline-edit-group"
                      label="Deadline:"
                      label-for="form-deadline-edit-input">
            <b-form-input id="form-deadline-edit-input"
                          type="text"
                          v-model="editForm.deadline"
                          required
                          placeholder="Enter deadline">
            </b-form-input>
          </b-form-group>
        <!-- <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group> -->
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      tasks: [],
      addTaskForm: {
        task: '',
        status: '',
        deadline: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        task: '',
        status: '',
        deadline: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTask(payload) {
      const path = 'http://localhost:5000/tasks';
      axios.post(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'Task added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getTasks();
        });
    },
    initForm() {
      this.addTaskForm.task = '';
      this.addTaskForm.status = '';
      this.addTaskForm.deadline = '';
      this.editForm.id = '';
      this.editForm.task = '';
      this.editForm.status = '';
      this.editForm.deadline = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      // let read = false;
      // if (this.addTaskForm.read[0]) read = true;
      const payload = {
        task: this.addTaskForm.task,
        status: this.addTaskForm.status,
        deadline: this.addTaskForm.deadline, // property shorthand
      };
      this.addTask(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      this.initForm();
    },
    editTask(task) {
      this.editForm = task;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTaskModal.hide();
      // let read = false;
      // if (this.editForm.read[0]) read = true;
      const payload = {
        task: this.editForm.task,
        status: this.editForm.status,
        deadline: this.editForm.deadline,
      };
      this.updateTask(payload, this.editForm.id);
    },
    updateTask(payload, taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios.put(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'Task updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTaskModal.hide();
      this.initForm();
      this.getTasks(); // why?
    },
    removeTask(taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios.delete(path)
        .then(() => {
          this.getTasks();
          this.message = 'task removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },
    onDeleteTask(task) {
      this.removeTask(task.id);
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
